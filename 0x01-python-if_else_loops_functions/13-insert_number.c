#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a linked list
 * @head: list head
 * @number: number to store the new node
 * Return: 0 always
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *aux = *head, *aux1;

	if (!head)
	{
		return (NULL);
	}

	node = malloc(sizeof(listint_t));
	if (!node)
	{
		return (NULL);
	}
	node->n = number;
	if (!aux || aux->n >= number)
	{
		node->next = aux, *head = node;
		return (node);
	}

	aux1 = aux->next;
	while (aux && aux1 && (aux1->n < number))
	{
		aux = aux->next, aux1 = aux->next;
	}

	aux->next = node, node->next = aux1;

	return (node);
}
