import random

# ------------------------
# Decorator for logging
# ------------------------
def log_training(func):
    def wrapper(*args, **kwargs):
        print("🔹 Starting:", func.__name__)
        result = func(*args, **kwargs)
        print("✅ Done:", func.__name__)
        return result
    return wrapper


# ------------------------
# Base Model Class (OOP + Encapsulation)
# ------------------------
class BaseModel:
    def __init__(self, name):
        self._name = name   # Encapsulation (_ means private)

    def __str__(self):
        return f"Model: {self._name}"

    def train(self, data):
        raise NotImplementedError("Subclass must implement train method.")

    def generate(self, prompt):
        raise NotImplementedError("Subclass must implement generate method.")


# ------------------------
# Child Model (Inheritance + Polymorphism)
# ------------------------
class TextGenerator(BaseModel):
    def __init__(self, name, vocab_size=1000):
        super().__init__(name)
        self.vocab_size = vocab_size

    @log_training   # Decorator use
    def train(self, data):
        print(f"Training {self._name} with {len(data)} samples...")

    def generate(self, prompt, length=10):
        words = [prompt]
        for _ in range(length):
            words.append(random.choice(["AI", "Python", "Generative", "Future"]))
        return " ".join(words)


# ------------------------
# Generator function for dataset (Memory Efficient)
# ------------------------
def data_generator(n):
    for i in range(n):
        yield f"Sample training text {i}"


# ------------------------
# Run Example
# ------------------------
if __name__ == "__main__":
    # Create object
    model = TextGenerator("MyGenAI", vocab_size=5000)
    print(model)

    # Load data using generator
    dataset = data_generator(5)
    data_list = list(dataset)  # convert to list
    print("Training Data:", data_list)

    # Train model
    model.train(data_list)

    # Generate text
    print("Generated:", model.generate("Hello"))
