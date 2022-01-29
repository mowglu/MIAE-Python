import altair as alt
import pandas as pd
import altair_viewer


def analyze(*, dataset: pd.DataFrame, airports_subset: list):
    data = pd.concat(
        (
            dataset.query(f'origin == "{airport}"')
                # count the number of departing aircraft per day
                .groupby("day")
                .agg(dict(callsign="count"))
                # label the current chunk with the name of the airport
                .rename(columns=dict(callsign=airport))
            # iterate on all airports in the list hereabove
            for airport in sum(airports_subset, [])
        ),
        axis=1,
    )
    return data


def visualize(data, airports_subset: list):
    chart = alt.Chart(
        data.reset_index()
            # prepare data for altair
            .melt("day", var_name="airport", value_name="count")
    )

    def full_chart(source, subset, subset_name):
        # We have many airports, only pick a subset
        chart = source.transform_filter(
            alt.FieldOneOfPredicate(field="airport", oneOf=subset)
        )

        # When we come close to a line, highlight it
        highlight = alt.selection(
            type="single", nearest=True, on="mouseover", fields=["airport"]
        )

        # The scatter plot
        points = (
            chart.mark_point()
                .encode(
                x="day",
                y=alt.Y("count", title="# of departing flights"),
                color=alt.Color("airport", legend=alt.Legend(title=subset_name)),
                # not too noisy please
                opacity=alt.value(0.5),
            )
                .add_selection(highlight)
        )

        # The trend plot
        lines = (
            chart.mark_line()
                .encode(
                x="day",
                y="count",
                color="airport",
                size=alt.condition(~highlight, alt.value(1), alt.value(3)),
            )
                # the cloud is a bit messy, draw a trend through it
                .transform_loess("day", "count", groupby=["airport"], bandwidth=0.2)
        )

        return lines + points

    # Concatenate several plots
    result = alt.vconcat(
        *[
            full_chart(chart, airport_, subset_name).properties(width=600, height=150)
            for subset_name, airport_ in zip(
                [
                    "European airports",
                    "East-Asian airports",
                    "Asian/Australian airports",
                    "American airports",
                ],
                airports_subset,
            )
        ]
    ).resolve_scale(color="independent")

    # Need to add something to visualize the figure explicitly (unlike Google Collab where it's easily viewable)
    altair_viewer.show(result)
    # This is not the world's best viewer, see if you can find alternatives!
