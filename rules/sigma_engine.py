from hunting.sigma_converter import sigma_to_hunt_query


class SigmaEngine:
    def compile_rule(self, rule_text: str):
        return sigma_to_hunt_query(rule_text)


sigma_engine = SigmaEngine()
