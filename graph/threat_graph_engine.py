from correlation.graph_builder import merge_alert_graphs


def build_threat_graph(alerts):
    return merge_alert_graphs(alerts)
