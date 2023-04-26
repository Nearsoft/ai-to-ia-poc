
class orchestrator:
    def __init__(self, plan):
        self.plan = plan


    def execute_plan(self):
        result = None

        for model in self.plan["model_sequence"]:
            model.execute(result)
            result = model.parse()

        return result