import InsectClass as i

def main():
    mosquito = i.Insect()
    fly = i.Insect()
    
    mosquito.lengthOfFlight()
    fly.lengthOfFlight()

    print(f'Mosquito flight in miles = {mosquito.getFlightDuration()}')
    print(f'Fly flight in miles = {fly.getFlightDuration()}')

if __name__ == "__main__":
    main()