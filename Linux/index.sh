#Find process with specific port
port=8080 && sudo ss -lptn "sport = :${port}"