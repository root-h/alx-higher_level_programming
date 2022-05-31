#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */

listint_t *insert_node(listint_t **head, int number);
