def custom_facet_title(fig, titles):
    for i, label in enumerate(titles):
        fig.layout.annotations[i]['text'] = label
    return fig
