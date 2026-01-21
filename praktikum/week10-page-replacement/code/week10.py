def fifo_page_replacement(pages, capacity):
    frame = []
    page_faults = 0
    for page in pages:
        if page not in frame:
            if len(frame) < capacity:
                frame.append(page)
            else:
                frame.pop(0)  # Hapus yang pertama masuk
                frame.append(page)
            page_faults += 1
        print(f"Reference {page}: Frame = {frame}, Faults = {page_faults}")
    return page_faults

def lru_page_replacement(pages, capacity):
    frame = []
    page_faults = 0
    for page in pages:
        if page not in frame:
            if len(frame) < capacity:
                frame.append(page)
            else:
                # Temukan yang paling lama digunakan (index terkecil)
                lru = min(set(frame), key=frame.index)
                frame.remove(lru)
                frame.append(page)
            page_faults += 1
        else:
            # Update posisi ke belakang (recently used)
            frame.remove(page)
            frame.append(page)
        print(f"Reference {page}: Frame = {frame}, Faults = {page_faults}")
    return page_faults

# Dataset uji
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3

print("=== SIMULASI FIFO ===")
fifo_faults = fifo_page_replacement(reference_string.copy(), frames)
print(f"\nTotal FIFO Page Faults: {fifo_faults}\n")

print("=== SIMULASI LRU ===")
lru_faults = lru_page_replacement(reference_string.copy(), frames)
print(f"\nTotal LRU Page Faults: {lru_faults}")
