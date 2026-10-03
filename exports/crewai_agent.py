from crewai import Agent

firmware_uefi_rootkit_detector = Agent(
    role="Firmware Uefi Rootkit Detector",
    goal="Deliver high-precision autonomous Firmware Uefi Rootkit Detector operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
