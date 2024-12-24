FROM python:3.10.16-alpine

# Install dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Copy and install dependencies
COPY pyproject.toml uv.lock /code/
RUN pip install .

# Copy the rest of the application code
COPY . /code/

# Copy and set the entrypoint script as executable
COPY ./scripts/entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

# Change ownership of the application code to the non-root user
RUN chown -R appuser:appgroup /code

# Switch to the non-root user
USER appuser

# Expose the port
EXPOSE 80

# Set the entrypoint
ENTRYPOINT ["sh", "/code/entrypoint.sh"]
