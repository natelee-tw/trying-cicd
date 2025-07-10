import streamlit as st
import requests
import random

def get_greeting():
    return "Hello, world! This is a Streamlit app."

def get_random_pokemon():
    """Fetch a random Pokemon from the PokeAPI"""
    try:
        # Get total number of Pokemon (up to 151 for original Pokemon)
        pokemon_id = random.randint(1, 151)
        
        # Fetch Pokemon data
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
        response.raise_for_status()
        
        pokemon_data = response.json()
        
        return {
            'name': pokemon_data['name'].title(),
            'id': pokemon_data['id'],
            'image_url': pokemon_data['sprites']['front_default'],
            'types': [type_info['type']['name'].title() for type_info in pokemon_data['types']]
        }
    except Exception as e:
        st.error(f"Error fetching Pokemon: {e}")
        return None

def main():
    st.title("🎮 Random Pokemon Generator")
    st.write("Press the button below to discover a random Pokemon!")
    
    if st.button("🎲 Get Random Pokemon"):
        with st.spinner("Finding a Pokemon for you..."):
            pokemon = get_random_pokemon()
            
            if pokemon:
                st.success(f"Found: {pokemon['name']}!")
                
                # Display Pokemon image
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.image(pokemon['image_url'], width=200, caption=f"#{pokemon['id']} {pokemon['name']}")
                
                with col2:
                    st.subheader(f"**{pokemon['name']}**")
                    st.write(f"**ID:** #{pokemon['id']}")
                    st.write(f"**Types:** {', '.join(pokemon['types'])}")
                    
                    # Add some fun facts
                    st.write("---")
                    st.write("✨ *A new Pokemon adventure awaits!*")

if __name__ == "__main__":
    main()
