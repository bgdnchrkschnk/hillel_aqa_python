import itertools

browsers = ["Chrome", "Firefox", "Safari"]
os = ["Windows", "Linux"]
versions = ["v1", "v2", "v3"]

obj = itertools.product(browsers, os, versions)
#
# for browser, os, version in obj:
#     print(browser, os, version)

# itter = iter(["Mykola", 24, "Kyiv"])
cycle_iter = itertools.cycle(["Mykola", 24, "Kyiv"])
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))



