#include "lists.h"

/**
 * insert_node - inserts a number into a linked list
 * @head: list head
 * @number: number to store the new node
 * Return: 0 always
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner;
	listint_t *new;

	runner = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (runner->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new->next = runner->next;
			runner->next = new;
			return (new);
		}
	}

	new->next = NULL;
	runner->next = new;
	return (new);
}
