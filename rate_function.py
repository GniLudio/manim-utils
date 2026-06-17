from collections.abc import Callable

from manim import Animation, AnimationGroup, linear, smooth


class RateFunction(AnimationGroup):
    def __init__(
        self,
        animation: Animation,
        rate_func: Callable[[float], float] = linear,
        **kwargs,
    ) -> None:
        super().__init__(animation, rate_func=rate_func, **kwargs)


class Smooth(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, smooth, **kwargs)


class Reverse(RateFunction):
    def __init__(self, animation: Animation, **kwargs) -> None:
        super().__init__(animation, lambda a: 1 - max(0, min(a, 1)), **kwargs)
