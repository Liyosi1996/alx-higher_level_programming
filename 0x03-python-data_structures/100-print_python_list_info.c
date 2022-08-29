#include <python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_p, allocated, num = 0;
	PyObject *element;

	size_p = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size_P);
	printf("[*] Allocated = %ld\n", allocated);
	while (num < size_p)
	{
		element = PyList_GET_ITEM(p, num);
		printf("Element %ld: %s\n", num, element->ob_type->tp_name);
		num++;
	}
}
