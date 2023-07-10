
from pyecharts import options as opts
from pyecharts.charts import Graph
nodes = [{
            "name": "Camel3942",
            "symbolSize": 5,
            "draggable": "False",
            "value": 1,
            "category": "Camel3942",
            "label": {
                "normal": {
                    "show": "True"
                }
            }
        },
        {
            "name": "Christinez",
            "symbolSize": 13,
            "draggable": "False",
            "value": 7,
            "category": "Christinez",
            "label": {
                "normal": {
                    "show": "True"
                }
            }
        },
        {
            "name": "JoannaBlue",
            "symbolSize": 5,
            "draggable": "False",
            "value": 1,
            "category": "JoannaBlue",
        }]
links = [{
            "source": "JoannaBlue",
            "target": "Christinez"
        },{
            "source": "JoannaBlue",
            "target": "Camel3942"
        }]


categories = [{
            "name": "Christinez"
        },
        {
            "name": "JoannaBlue"
        },{
        'mane':'Camel3942'
    }]

c = (
    Graph()
        .add(
        "",
        nodes,
        links,
        categories,
        repulsion=50,
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False),
    )
        .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="Graph-微博转发关系图"),
    )
        .render("graph.html")
)
