# Judul: Simulasi Page Replacement FIFO vs LRU

def simulate_fifo(pages, frames_count):
    memory = []
    result = []
    faults = 0
    
    for page in pages:
        status = "HIT"
        if page not in memory:
            status = "MISS"
            faults += 1
            if len(memory) < frames_count:
                memory.append(page)
            else:
                memory.pop(0) 
                memory.append(page)
        
        result.append({
            "page": page,
            "memory": list(memory),
            "status": status
        })
    return result, faults

def simulate_lru(pages, frames_count):
    memory = []
    result = []
    faults = 0
    
    for page in pages:
        status = "HIT"
        if page not in memory:
            status = "MISS"
            faults += 1
            if len(memory) < frames_count:
                memory.append(page)
            else:
                memory.pop(0) 
                memory.append(page)
        else:
            
            memory.remove(page)
            memory.append(page)
            
        result.append({
            "page": page,
            "memory": list(memory),
            "status": status
        })
    return result, faults

def print_table(title, data, total_faults, n_pages):
    print(f"\n{title}")
    print("-" * 50)
    print("Step | Page | Current Memory State       | Status")
    print("-" * 50)
    for i, step in enumerate(data):
        mem_str = str(step['memory']).ljust(25)
        print(f"{i+1:>4} | {step['page']:>4} | {mem_str} | {step['status']}")
    
    print("-" * 50)
    print(f"Total Page Faults : {total_faults}")
    print(f"Fault Rate        : {(total_faults / n_pages) * 100:.2f}%")


reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
frames = 3

print("\n=== ANALISIS PAGE REPLACEMENT ===")
print(f"Reference String : {reference_string}")
print(f"Kapasitas Frame  : {frames}")

# UJI COBA 1: FIFO
data_fifo, faults_fifo = simulate_fifo(reference_string, frames)
print_table("FIFO Replacement Result", data_fifo, faults_fifo, len(reference_string))

# UJI COBA 2: LRU
data_lru, faults_lru = simulate_lru(reference_string, frames)
print_table("LRU Replacement Result", data_lru, faults_lru, len(reference_string))