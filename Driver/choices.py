

USER = (
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('personnel', 'Personnel'),
    ('dispatcher', 'Dispatcher'),
    ('forwarder', 'Forwarder'),
    ('driver', 'Driver'),
)

STATUS = (
    ("positive", "Positive"),
)

STATUS_PROBLEM = (
    ("positive", "Positive"),
    ("Raport problem", "Raport problem")
)

NUMBER = (
    ("PL", "+48"),
    ("DE", "+49"),
    ("I", "+39"),
)

DRIVER_LICENSE = (
    ("b", "B"),
    ("B+E", "B+E"),
    ("C", "C"),
    ("C+E", "C+E"),
)

COUNTRY = (
    ("AL", "Albania"),
    ("AD", "Andorra"),
    ("AT", "Austria"),
    ("BY", "Belarus"),
    ("BE", "Belgium"),
    ("BA", "Bosnia and Herzegovina"),
    ("BG", "Bulgaria"),
    ("HR", "Croatia"),
    ("CY", "Cyprus"),
    ("CZ", "Czech Republic"),
    ("DK", "Denmark"),
    ("EE", "Estonia"),
    ("FI", "Finland"),
    ("FR", "France"),
    ("DE", "Germany"),
    ("UK", "United Kingdom"),
    ("GR", "Greece"),
    ("HU", "Hungary"),
    ("IS", "Iceland"),
    ("IRL", "Ireland"),
    ("IT", "Italy"),
    ("LV", "Latvia"),
    ("LI", "Liechtenstein"),
    ("LT", "Lithuania"),
    ("LU", "Luxembourg"),
    ("MK", "Macedonia"),
    ("MT", "Malta"),
    ("MD", "Moldova"),
    ("MC", "Monaco"),
    ("ME", "Montenegro"),
    ("NL", "Netherlands"),
    ("NO", "Norway"),
    ("PL", "Poland"),
    ("PT", "Portugal"),
    ("RO", "Romania"),
    ("RU", "Russia"),
    ("SM", "San Marino"),
    ("RS", "Serbia"),
    ("SK", "Slovakia"),
    ("SI", "Slovenia"),
    ("ES", "Spain"),
    ("SE", "Sweden"),
    ("CH", "Switzerland"),
    ("TR", "Turkey"),
    ("UA", "Ukraine"),
    ("VA", "Vatican"),
)

TRUCK = (
    ("bus", "Bus"),
    ("bus trailer", "Bus Trailer"),
    ("small truck", "Small Truck"),
    ("solo", "Solo"),
    ("truck tandem", "Truck Tandem"),
    ("truck trailer", "Truck Trailer"),
)

TRUCK_SPACE = (
    ('truck', 'Truck'),
    ('8', '8 euro pallets'),
    ('9', '9 euro pallets'),
    ('10', '10 euro pallets'),
    ('12', '12 euro pallets'),
    ('18', '18 euro pallets'),
    ('19', '19 euro pallets'),

)

TRAILER = (
    ('tilt trailer', 'Tilt Trailer'),
    ('Refrigerator Trailer', 'Refrigerator Trailer'),
    ('container trailer', 'Container Trailer'),
    ('trailer floor', 'Trailer Floor'),
    ('trailer moving floor', 'Trailer Moving floor'),
    ('special trailer', 'Special Trailer'),
    ('isothermal trailer', 'Isothermal Trailer'),
    ('tank trailer', 'Tank Trailer'),
)

TRAILER_SPACE = (
    ('8', '8 euro pallets'),
    ('9', '9 euro pallets'),
    ('10', '10 euro pallets'),
    ('12', '12 euro pallets'),
    ('18', '18 euro pallets'),
    ('19', '19 euro pallets'),
    ('20', '20 euro pallets'),
    ('32', '32 euro pallets'),
    ('33', '33 euro pallets'),
    ('36', '36 euro pallets'),
)

FIX = (
    ('fix', 'FIX'),
    ('free', ''),
)

CUSTOMS_CLEARANCE = (
    ('customs', 'CUSTOMS'),
    ('free', '')
)