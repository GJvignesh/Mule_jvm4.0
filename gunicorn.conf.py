import multiprocessing

bind = "0.0.0.0:5000"  # here we are picking the port 5000 which can be changed later
#workers = multiprocessing.cpu_count() * 2 + 1
workers = 4 # going with 4 worker modules