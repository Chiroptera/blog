Title: SciPy's CSR matrix problem
Date: 07-09-2015
Category: 
Tags: python, scipy


While creating a CSR matrix the SciPy *_cs_matrix* class computes the appropriate datatype for the *indices* and *indptr* arrays. For the matrix to work the *indptr* must have a datatype that can index the number of non-zero values existent in the matrix and the *indices* array must have  a datatype that can index the number of columns. For my use, the number of non-zero elements is much bigger than the number of columns, which usually means that the datatypes if *indices* and *indptr* are *numpy.int32* and *numpy.int64*, respectively.

The problem is that the class uses the same datatype for both arrays and then the *indices* array doesn't fit in memory. It first does this in the *scipy/sparse/compressed.py* file at the *__init__* method. As such, I changed this

```python
elif len(arg1) == 3:
    # (data, indices, indptr) format
    (data, indices, indptr) = arg1
    idx_dtype = get_index_dtype((indices, indptr), check_contents=True)
    self.indices = np.array(indices, copy=copy, dtype=idx_dtype)
    self.indptr = np.array(indptr, copy=copy, dtype=idx_dtype)
    self.data = np.array(data, copy=copy, dtype=getdtype(dtype, data))
```

to this

```python
elif len(arg1) == 3:
    (data, indices, indptr) = arg1
    indptr_dtype = get_index_dtype(maxval=indices.size)
    indices_dtype = get_index_dtype(maxval=indptr.size-1)
    self.indices = np.array(indices, copy=copy, dtype=indices_dtype)
    self.indptr = np.array(indptr, copy=copy, dtype=indptr_dtype)
    self.data = np.array(data, copy=copy, dtype=getdtype(dtype, data))
```

Then I found that this was happening in yet another place, in the same file, when the *__init__* method calls the *self.check_format(full_check=False)* method. So I had to do the same this as before, with a slight change. I changed this

```python
idx_dtype = get_index_dtype((self.indptr, self.indices))
self.indptr = np.asarray(self.indptr, dtype=idx_dtype)
self.indices = np.asarray(self.indices, dtype=idx_dtype)
self.data = to_native(self.data)
```

to this

```python
indptr_dtype = get_index_dtype(maxval=self.indices.size)
indices_dtype = get_index_dtype(maxval=self.indptr.size-1)
self.indices = np.array(self.indices, dtype=indices_dtype)
self.indptr = np.array(self.indptr, dtype=indptr_dtype)
self.data = to_native(self.data)
```