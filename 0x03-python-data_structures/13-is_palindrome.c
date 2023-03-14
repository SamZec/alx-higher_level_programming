#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head);
listint_t *reverse_listint(listint_t **head);
listint_t *middle_listint(listint_t **head);

/**
 * middle_listint - sets pointer to middle of linked list
 * @head: pointer to first node
 *
 * Return: pointer to middle node
 */
listint_t *middle_listint(listint_t **head)
{
	listint_t *slow, *fast;

	fast = slow = (*head);
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow);
}

/**
 * reverse_listint -  reverses a listint_t linked list.
 * @head: pointer to head node in listint_t list.
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *ahead, *behind;

	if (head == NULL || *head == NULL)
		return (NULL);

	behind = NULL;

	while ((*head)->next != NULL)
	{
		ahead = (*head)->next;
		(*head)->next = behind;
		behind = *head;
		*head = ahead;
	}

	(*head)->next = behind;

	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to first node in list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev, *mid, *current;

	if (head == NULL || *head == NULL)
		return (1);

	current = (*head);
	mid = middle_listint(head);
	rev = reverse_listint(&mid->next);

	while (rev != NULL)
	{
		if (current->n != rev->n)
			return (0);
		rev = rev->next;
		current = current->next;
	}
	return (1);
}
