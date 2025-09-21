import MarshalDecoder

print("Available functions/objects in MarshalDecoder")
print(dir(MarshalDecoder))

if hasattr(MarshalDecoder, "main"):
    MarshalDecoder.main()
elif hasattr(MarshalDecoder, "start"):
    MarshalDecoder.start()
else:
    print("No main/start function found.")
