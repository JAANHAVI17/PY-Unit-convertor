from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QComboBox, QLineEdit, QLabel, QPushButton, 
                            QStackedWidget, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class ConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ultimate Unit Converter")
        self.setGeometry(100, 100, 650, 450)
        self.setMinimumSize(550, 400)
        
        # Set application-wide palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        self.setPalette(palette)
        
        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Category selection
        self.category_combo = QComboBox()
        self.category_combo.addItems(["Length", "Weight", "Temperature", "Area", "Volume", "Time", "Speed"])
        self.category_combo.setFont(QFont("Segoe UI", 12))
        self.category_combo.setFixedHeight(40)
        
        # Stacked widget for different converters
        self.stacked_widget = QStackedWidget()
        
        # Create all converter pages
        self.create_converter_pages()
        
        # Add widgets to main layout
        main_layout.addWidget(QLabel("Select Conversion Type:"))
        main_layout.addWidget(self.category_combo)
        main_layout.addWidget(self.stacked_widget)
        
        # Connect signals
        self.category_combo.currentIndexChanged.connect(self.change_category)
    
    def create_converter_pages(self):
        """Create all converter pages and store references to their widgets"""
        self.converters = []
        
        # Length converter
        length_units = ["Millimeters (mm)", "Centimeters (cm)", "Meters (m)", 
                       "Kilometers (km)", "Inches (in)", "Feet (ft)", 
                       "Yards (yd)", "Miles (mi)"]
        self.converters.append(self.create_converter_frame(length_units))
        
        # Weight converter
        weight_units = ["Milligrams (mg)", "Grams (g)", "Kilograms (kg)", 
                       "Metric tons (t)", "Ounces (oz)", "Pounds (lb)", 
                       "Stones (st)", "US tons"]
        self.converters.append(self.create_converter_frame(weight_units))
        
        # Temperature converter
        temp_units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
        self.converters.append(self.create_converter_frame(temp_units))
        
        # Area converter
        area_units = ["Square millimeters (mm²)", "Square centimeters (cm²)", 
                     "Square meters (m²)", "Hectares (ha)", "Square kilometers (km²)", 
                     "Square inches (in²)", "Square feet (ft²)", "Square yards (yd²)", 
                     "Acres (ac)", "Square miles (mi²)"]
        self.converters.append(self.create_converter_frame(area_units))
        
        # Volume converter
        volume_units = ["Milliliters (ml)", "Centiliters (cl)", "Deciliters (dl)", 
                       "Liters (l)", "Cubic centimeters (cm³)", "Cubic meters (m³)", 
                       "Teaspoons (tsp)", "Tablespoons (tbsp)", "Fluid ounces (fl oz)", 
                       "Cups (cup)", "Pints (pt)", "Quarts (qt)", "Gallons (gal)"]
        self.converters.append(self.create_converter_frame(volume_units))
        
        # Time converter
        time_units = ["Nanoseconds (ns)", "Microseconds (µs)", "Milliseconds (ms)", 
                      "Seconds (s)", "Minutes (min)", "Hours (h)", 
                      "Days (d)", "Weeks (wk)", "Months (mo)", "Years (yr)"]
        self.converters.append(self.create_converter_frame(time_units))
        
        # Speed converter
        speed_units = ["Meters per second (m/s)", "Kilometers per hour (km/h)", 
                       "Miles per hour (mph)", "Feet per second (ft/s)", 
                       "Knots (kn)", "Mach (at std. atm.)"]
        self.converters.append(self.create_converter_frame(speed_units))
        
        # Add all converters to stacked widget
        for converter in self.converters:
            self.stacked_widget.addWidget(converter)
    
    def create_converter_frame(self, units):
        """Create a converter frame with input/output fields and buttons"""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Input section
        input_layout = QHBoxLayout()
        input_value = QLineEdit()
        input_value.setPlaceholderText("Enter value...")
        input_value.setAlignment(Qt.AlignRight)
        input_value.setFont(QFont("Segoe UI", 14))
        input_unit = QComboBox()
        input_unit.addItems(units)
        input_unit.setFont(QFont("Segoe UI", 12))
        
        input_layout.addWidget(input_value, 3)
        input_layout.addWidget(input_unit, 2)
        
        # Output section
        output_layout = QHBoxLayout()
        output_value = QLineEdit()
        output_value.setReadOnly(True)
        output_value.setAlignment(Qt.AlignRight)
        output_value.setFont(QFont("Segoe UI", 14))
        output_unit = QComboBox()
        output_unit.addItems(units)
        output_unit.setFont(QFont("Segoe UI", 12))
        
        output_layout.addWidget(output_value, 3)
        output_layout.addWidget(output_unit, 2)
        
        # Buttons
        button_layout = QHBoxLayout()
        convert_btn = QPushButton("Convert")
        convert_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        convert_btn.setFixedHeight(40)
        
        swap_btn = QPushButton("↔ Swap Units")
        swap_btn.setFont(QFont("Segoe UI", 11))
        swap_btn.setFixedHeight(35)
        
        button_layout.addWidget(convert_btn)
        button_layout.addWidget(swap_btn)
        
        # Add widgets to layout
        layout.addLayout(input_layout)
        layout.addLayout(output_layout)
        layout.addLayout(button_layout)
        
        # Store references to widgets as frame properties
        frame.input_value = input_value
        frame.input_unit = input_unit
        frame.output_value = output_value
        frame.output_unit = output_unit
        
        # Connect buttons
        convert_btn.clicked.connect(lambda: self.convert_units(frame))
        swap_btn.clicked.connect(lambda: self.swap_units(frame))
        
        return frame
    
    def change_category(self, index):
        """Switch between different converter pages"""
        self.stacked_widget.setCurrentIndex(index)
    
    def swap_units(self, frame):
        """Swap input and output units"""
        current_input = frame.input_unit.currentIndex()
        current_output = frame.output_unit.currentIndex()
        frame.input_unit.setCurrentIndex(current_output)
        frame.output_unit.setCurrentIndex(current_input)
        
        # Also swap values if output has a value
        if frame.output_value.text():
            frame.input_value.setText(frame.output_value.text())
            self.convert_units(frame)
    
    def convert_units(self, frame):
        """Perform the unit conversion"""
        try:
            value = float(frame.input_value.text())
        except ValueError:
            frame.output_value.setText("Invalid input")
            return
            
        category = self.category_combo.currentText()
        from_unit = frame.input_unit.currentText()
        to_unit = frame.output_unit.currentText()
        
        # Special handling for temperature
        if category == "Temperature":
            result = self.convert_temperature(value, from_unit, to_unit)
            frame.output_value.setText(f"{result:.2f}")
            return
            
        # Get conversion factors
        conversion_factors = self.get_conversion_factors(category)
        
        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            frame.output_value.setText("Conversion not available")
            return
            
        # Convert to base unit first, then to target unit
        base_value = value * conversion_factors[from_unit]
        result = base_value / conversion_factors[to_unit]
        frame.output_value.setText(f"{result:.6g}")
    
    def convert_temperature(self, value, from_unit, to_unit):
        """Special conversion for temperature units"""
        # Convert to Celsius first
        if "Celsius" in from_unit:
            celsius = value
        elif "Fahrenheit" in from_unit:
            celsius = (value - 32) * 5/9
        elif "Kelvin" in from_unit:
            celsius = value - 273.15
        
        # Convert from Celsius to target unit
        if "Celsius" in to_unit:
            return celsius
        elif "Fahrenheit" in to_unit:
            return (celsius * 9/5) + 32
        elif "Kelvin" in to_unit:
            return celsius + 273.15
    
    def get_conversion_factors(self, category):
        """Return conversion factors for the given category"""
        factors = {
            "Length": {
                "Millimeters (mm)": 0.001,
                "Centimeters (cm)": 0.01,
                "Meters (m)": 1.0,
                "Kilometers (km)": 1000.0,
                "Inches (in)": 0.0254,
                "Feet (ft)": 0.3048,
                "Yards (yd)": 0.9144,
                "Miles (mi)": 1609.34
            },
            "Weight": {
                "Milligrams (mg)": 1e-6,
                "Grams (g)": 0.001,
                "Kilograms (kg)": 1.0,
                "Metric tons (t)": 1000.0,
                "Ounces (oz)": 0.0283495,
                "Pounds (lb)": 0.453592,
                "Stones (st)": 6.35029,
                "US tons": 907.185
            },
            "Area": {
                "Square millimeters (mm²)": 1e-6,
                "Square centimeters (cm²)": 0.0001,
                "Square meters (m²)": 1.0,
                "Hectares (ha)": 10000.0,
                "Square kilometers (km²)": 1e6,
                "Square inches (in²)": 0.00064516,
                "Square feet (ft²)": 0.092903,
                "Square yards (yd²)": 0.836127,
                "Acres (ac)": 4046.86,
                "Square miles (mi²)": 2.59e6
            },
            "Volume": {
                "Milliliters (ml)": 0.001,
                "Centiliters (cl)": 0.01,
                "Deciliters (dl)": 0.1,
                "Liters (l)": 1.0,
                "Cubic centimeters (cm³)": 0.001,
                "Cubic meters (m³)": 1000.0,
                "Teaspoons (tsp)": 0.00492892,
                "Tablespoons (tbsp)": 0.0147868,
                "Fluid ounces (fl oz)": 0.0295735,
                "Cups (cup)": 0.236588,
                "Pints (pt)": 0.473176,
                "Quarts (qt)": 0.946353,
                "Gallons (gal)": 3.78541
            },
            "Time": {
                "Nanoseconds (ns)": 1e-9,
                "Microseconds (µs)": 1e-6,
                "Milliseconds (ms)": 0.001,
                "Seconds (s)": 1.0,
                "Minutes (min)": 60.0,
                "Hours (h)": 3600.0,
                "Days (d)": 86400.0,
                "Weeks (wk)": 604800.0,
                "Months (mo)": 2.628e6,
                "Years (yr)": 3.154e7
            },
            "Speed": {
                "Meters per second (m/s)": 1.0,
                "Kilometers per hour (km/h)": 0.277778,
                "Miles per hour (mph)": 0.44704,
                "Feet per second (ft/s)": 0.3048,
                "Knots (kn)": 0.514444,
                "Mach (at std. atm.)": 343.0
            }
        }
        
        return factors.get(category, {})