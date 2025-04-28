class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """
        Convert temperature from Celsius to Fahrenheit.
        
        Args:
            c (float): Temperature in Celsius
            
        Returns:
            float: Temperature in Fahrenheit
        """
        return (c * 9/5) + 32 
    