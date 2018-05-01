
import numpy as np
my_list = [1,2,3]

#convert list to np array
np.array(my_list)

#create arange of array
np.arange(0,10)

#create zeros array
np.zeros(3)

#create zeros array multidimension
np.zeros((3,5))

#create ones array same with zeros function
np.ones((3,4))

#create aray linespace
np.linspace(0,5,10)


#create random integer
np.random.randint(0,100)

#create random integer
np.random.randint(0,100,5)

#create random integer
np.random.randint(0,100,(5,3))

np.random.seed(123)
np.random.randint(0,4,3)

np.random.seed(123)
np.random.randint(0,4,3)

np.random.randint(0,4,3)

np.random.seed(1)
np.random.randint(0,4,20)


np.random.seed(1)
np.random.randint(0,100,50)


np.random.seed(1)
arr = np.random.randint(0,100,50)

arr

arr.max()

arr.min()

arr.mean()

#index max position
arr.argmax()

arr.reshape(5,10)

mat = np.arange(0,100).reshape(10,10)

mat

#get number from array
mat[4,3]

#get all but only column
mat[:,0]

#get all but only row
mat[6,:]
mat[0:3,0:4]
mat > 70
my_filter = mat > 70
mat[my_filter]
print(mat[mat>70])

