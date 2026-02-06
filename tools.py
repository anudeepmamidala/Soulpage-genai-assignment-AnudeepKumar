# tools.py
import time


def web_search(query: str) -> str:
    """Search Wikipedia for factual information."""
    return wikipedia_search(query)


def wikipedia_search(query: str) -> str:
    """Search Wikipedia and return concise answer."""
    try:
        import wikipedia as wiki
        wiki.set_lang("en")
        
        print(f"[Searching Wikipedia for: {query}]")
        
        # Get summary - just 2 sentences for cleaner answers
        summary = wiki.summary(query, sentences=2, auto_suggest=True)
        
        print(f"[Found Wikipedia article]")
        return summary
        
    except ImportError:
        return "Wikipedia not installed."
    except Exception as e:
        if "DisambiguationError" in str(type(e)):
            # Try to get first option
            try:
                options = str(e).split('\n')[1:4]
                return f"Multiple results. Try: {', '.join(options)}"
            except:
                return "Multiple results found. Please be more specific."
        elif "PageError" in str(type(e)):
            return "No Wikipedia page found."
        else:
            return f"Search error: {str(e)}"


# Test
if __name__ == "__main__":
    print("Testing Wikipedia search...")
    print("="*50)
    
    tests = [
        "Sundar Pichai",
        "Paris",
        "Python programming language"
    ]
    
    for query in tests:
        print(f"\nQuery: {query}")
        print(f"Result: {web_search(query)}\n")
        time.sleep(1)