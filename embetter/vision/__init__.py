from embetter.error import NotInstalled
from embetter.vision._grab import ImageGrabber
from embetter.vision._colorhist import ColorHistogramEncoder

try:
    from embetter.vision._torchvis import TimmEncoder
except ModuleNotFoundError:
    TorchVision = NotInstalled("TorchImageModel", "vision")


__all__ = ["ImageGrabber", "ColorHistogram", "TorchImageModel"]
