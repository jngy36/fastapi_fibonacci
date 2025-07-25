from fastapi import FastAPI, HTTPException
from typing import Dict
import time

app = FastAPI(
    title="Fibonacci Calculator API",
    description="A simple API to calculate Fibonacci numbers",
    version="1.0.0"
)

def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using iterative approach for efficiency."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Fibonacci Calculator API",
        "endpoints": {
            "/fibonacci/{n}": "Calculate the nth Fibonacci number",
            "/docs": "API documentation"
        }
    }

@app.get("/fibonacci/{n}")
async def calculate_fibonacci(n: int) -> Dict[str, any]:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence (non-negative integer)
        
    Returns:
        Dictionary containing the input, result, and calculation time
    """
    if n < 0:
        raise HTTPException(
            status_code=400, 
            detail="Fibonacci is not defined for negative numbers"
        )
    
    if n > 10000:  # Prevent extremely large calculations
        raise HTTPException(
            status_code=400,
            detail="Number too large. Please use n <= 10000"
        )
    
    start_time = time.time()
    try:
        result = fibonacci(n)
        calculation_time = time.time() - start_time
        
        return {
            "input": n,
            "fibonacci": result,
            "calculation_time_seconds": round(calculation_time, 6)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fibonacci/sequence/{count}")
async def fibonacci_sequence(count: int) -> Dict[str, any]:
    """
    Generate a sequence of Fibonacci numbers.
    
    Args:
        count: Number of Fibonacci numbers to generate
        
    Returns:
        Dictionary containing the sequence and metadata
    """
    if count < 1:
        raise HTTPException(
            status_code=400,
            detail="Count must be a positive integer"
        )
    
    if count > 100:  # Prevent extremely large sequences
        raise HTTPException(
            status_code=400,
            detail="Count too large. Please use count <= 100"
        )
    
    start_time = time.time()
    sequence = [fibonacci(i) for i in range(count)]
    calculation_time = time.time() - start_time
    
    return {
        "count": count,
        "sequence": sequence,
        "calculation_time_seconds": round(calculation_time, 6)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
