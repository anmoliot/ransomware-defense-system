def correlate_cloud_endpoint(cloud_events, endpoint_alerts):
    risky_cloud = [event for event in cloud_events if event.get("risky")]
    return {"cloud_events": len(risky_cloud), "endpoint_alerts": len(endpoint_alerts), "xdr_match": bool(risky_cloud and endpoint_alerts)}
