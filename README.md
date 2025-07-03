| Method | Endpoint             | Description                 | Auth Required?         |
| ------ | -------------------- | --------------------------- | ---------------------- |
| GET    | `/`                  | Welcome message             | No                     |
| GET    | `/quotes`            | Get a random quote          | No                     |
| GET    | `/quotes/{quote_id}` | Get quote by ID             | No                     |
| POST   | `/quotes`            | Add a new quote             | Yes (x-api-key header) |
| PUT    | `/quotes/{quote_id}` | Update existing quote by ID | Yes (x-api-key header) |
| DELETE | `/quotes/{quote_id}` | Delete a quote by ID        | Yes (x-api-key header) |
