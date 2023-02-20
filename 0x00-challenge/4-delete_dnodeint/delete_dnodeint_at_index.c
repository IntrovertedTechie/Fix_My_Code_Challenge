#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
/**
 * delete_dnodeint_at_index - Deletes a node at a given position
 *
 * @head: A pointer to a pointer to the first element of the list
 * @index: The index of the node to delete
 *
 * Return: 1 if success, -1 otherwise
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current, *tmp;
	unsigned int i;

	if (*head == NULL)
		return (-1);

	current = *head;
	if (index == 0)
	{
		*head = current->next;
		if (current->next)
			current->next->prev = NULL;
		free(current);
		return (1);
	}

	for (i = 0; current && i < index - 1; i++)
		current = current->next;

	if (current == NULL || current->next == NULL)
		return (-1);

	tmp = current->next;
	current->next = tmp->next;
	if (tmp->next)
		tmp->next->prev = current;
	free(tmp);

	return (1);
}

