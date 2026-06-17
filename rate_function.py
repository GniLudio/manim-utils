from collections.abc import Callable

from manim import Animation, AnimationGroup
from manim.utils import rate_functions


class RateFunction(AnimationGroup):
    def __init__(
        self,
        animation: Animation,
        rate_func: Callable[[float], float] = rate_functions.linear,
        **kwargs,
    ) -> None:
        super().__init__(animation, rate_func=rate_func, **kwargs)


class Reverse(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, lambda a: 1 - a, **kwargs)


class Linear(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.linear, **kwargs)


class Smooth(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.smooth, **kwargs)


class SmoothStep(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.smoothstep, **kwargs)


class SmootherStep(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.smootherstep, **kwargs)


class SmoothererStep(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.smoothererstep, **kwargs)


class RushInto(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.rush_into, **kwargs)


class RushFrom(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.rush_from, **kwargs)


class SlowInto(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.slow_into, **kwargs)


class DoubleSmooth(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.double_smooth, **kwargs)


class RunningStart(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.running_start, **kwargs)


class Lingering(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.lingering, **kwargs)


class ExponentialDecay(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.exponential_decay, **kwargs)


class EaseInSine(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_sine, **kwargs)


class EaseOutSine(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_sine, **kwargs)


class EaseInOutSine(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_sine, **kwargs)


class EaseInQuad(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_quad, **kwargs)


class EaseOutQuad(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_quad, **kwargs)


class EaseInOutQuad(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_quad, **kwargs)


class EaseInCubic(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_cubic, **kwargs)


class EaseOutCubic(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_cubic, **kwargs)


class EaseInOutCubic(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_cubic, **kwargs)


class EaseInQuart(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_quart, **kwargs)


class EaseOutQuart(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_quart, **kwargs)


class EaseInOutQuart(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_quart, **kwargs)


class EaseInQuint(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_quint, **kwargs)


class EaseOutQuint(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_quint, **kwargs)


class EaseInOutQuint(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_quint, **kwargs)


class EaseOnExpo(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_expo, **kwargs)


class EaseOutExpo(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_expo, **kwargs)


class EaseInOutExpo(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_expo, **kwargs)


class EaseInCirc(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_circ, **kwargs)


class EaseOutCirc(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_circ, **kwargs)


class EaseInOutCirc(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_circ, **kwargs)


class EaseInBack(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_back, **kwargs)


class EaseOutBack(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_back, **kwargs)


class EaseInOutBack(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_back, **kwargs)


class EaseInElastic(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_elastic, **kwargs)


class EaseOutElastic(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_elastic, **kwargs)


class EaseInOutElastic(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_elastic, **kwargs)


class EaseInBounce(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_bounce, **kwargs)


class EaseOutBounce(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_out_bounce, **kwargs)


class EaseInOutBounce(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, rate_functions.ease_in_out_bounce, **kwargs)
