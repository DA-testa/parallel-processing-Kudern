# python3
import heapq

def parallel_processing(n, m, data):
    # Create a list of tuples for the heap queue
    threads = [(0, i) for i in range(n)]
    output = []

    for i in range(m):
        # Pop the thread that finishes earliest
        time, index = heapq.heappop(threads)
        output.append((index, time))

        # Add the next job to the thread, increment its time
        heapq.heappush(threads, (time + data[i], index))
    
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)

    for i in result:
        print(i[0], i[1])

if __name__ == "__main__":
    main()
