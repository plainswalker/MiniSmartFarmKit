import inputmodules
import outputmodules
import commodule

inputmodules.run()

commodule.init(ims=inputmodules.modules(), oms=outputmodules.modules())
while True:
    try:
        commodule.update()
    except KeyboardInterrupt:
        exit()
    except Exception as e:
    	print(e)
