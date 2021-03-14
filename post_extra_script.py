import os
Import("env", "projenv")

# access to global construction environment
#print(env)

# Dump construction environment (for debug purpose)
#print(env.Dump())


def after_build(source, target, env):
    all = env.GetProjectOptions("board")
    print(all["board"])
    print("Calling aggregate shell script")
    env.Execute("./aggregate_bin.sh " + all["board"])

env.AddPostAction("buildprog", after_build)
