class MessageValidator:

    def validate(self, message):

        checks = {

            "length": len(message) < 500,

            "contains_cta":
                "?" in message,

            "has_specificity":
                any(
                    char.isdigit()
                    for char in message
                )
        }

        return checks