VM_MARKERS = ("vbox", "vmware", "qemu", "hyper-v", "xen")


def detect_vm_markers(strings):
    return [item for item in strings if any(marker in item.lower() for marker in VM_MARKERS)]
