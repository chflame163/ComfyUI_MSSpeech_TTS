
class AnyType(str):
  """always equal in 'not equal comparisons(__ne__)' """

  def __ne__(self, __value: object) -> bool:
    return False

any = AnyType("*")


class Trigger:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "always_true": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "anything": (any, {}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "check_input"
    OUTPUT_NODE = True
    CATEGORY = "MicrosoftSpeech_TTS"

    def check_input(self, always_true, anything=None):

        ret = False
        if always_true or (anything is not None):
            ret = True
        print(f"Input Trigger: {ret}")

        return (ret,)


NODE_CLASS_MAPPINGS = {
    "Input Trigger": Trigger
}
