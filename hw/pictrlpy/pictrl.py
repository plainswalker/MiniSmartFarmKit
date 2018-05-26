import inputmodules
import outputmodules
import commodule

inputmodules.run()

commodule.init(ims=inputmodules.modules(), oms=outputmodules.modules())
try:
    commodule.run()
except KeyboardInterrupt:
    exit()
