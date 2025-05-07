# HTTP-code-dog-images
Database Query Complexity Explanation
1. User Authentication (Login/Signup):

Operation: Insert and select user credentials.

Complexity:

Signup: O(1) for inserting new user record.

Login: O(1) lookup using indexed email/username.

Reason: Operations use primary keys or unique fields with indexes (e.g., email), which are constant time in SQL databases like SQLite.

2. Saving/Updating/Deleting Code Lists:

Operation:

Save: INSERT INTO a user-specific list table.

Edit: UPDATE list based on list ID and user ID.

Delete: DELETE from list by ID.

Complexity: All are O(1) assuming proper indexing on user_id and list_id.

3. Search/Filter for HTTP Status Codes:

Operation: Search/filter based on status code (e.g., 404, 200).

Complexity:

O(1) for exact-match search using indexed status code.

O(n) if filtering based on text input without an index.

Optimization: Used dictionary-based mapping for fast status-to-URL resolution without hitting external APIs repeatedly.
