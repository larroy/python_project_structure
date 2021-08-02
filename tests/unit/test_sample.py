from examplepkg.samplemodule import sample_fun_times_two


def test_fun():
    "Test that sample_fun_times_two doubles its argument."
    assert sample_fun_times_two(5) == 10
