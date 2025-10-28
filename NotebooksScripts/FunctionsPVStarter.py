"""
Functions, Classes and Modules Tutorial
This file demonstrates Python functions.

Learning objectives:
- Defining and using functions

Complete the script by filling in the missing code sections marked with <---.

@author: PLACE YOUR NAME HERE
"""

# Import any necessary libraries
import math
# (pd, np, os are unused here—remove if not needed)

# <--- Define a function to size a PV system based on building dimensions and panel specifications
def calculate_pv_size(
    building_length_m: float,
    building_width_m: float,
    roof_angle_deg: float,
    panel_width_mm: float = 1046,   # SunPower Maxeon 400 Wp (approx.)
    panel_height_mm: float = 1690,  # defaults in mm
    panel_power_Wp: float = 400
):  # <--- include parameters for building length, width, roof angle, panel width, panel height and panel power
    """
    Calculate PV array size that fits on a rectangular mono-pitch roof (no overhang).

    Parameters
    ----------
    building_length_m : float
        Building length along the ridge/eaves (meters).
    building_width_m : float
        Horizontal plan-view width (meters).
    roof_angle_deg : float
        Roof pitch angle from horizontal (degrees).
    panel_width_mm : float, optional
        PV panel width in millimeters.
    panel_height_mm : float, optional
        PV panel height in millimeters.
    panel_power_Wp : float, optional
        Panel nameplate power in Wp.

    Returns
    -------
    total_capacity_kW : float
        Total PV capacity that fits on the roof, in kW.
    n_panels : int
        Number of panels placed (best of portrait/landscape).

    Notes
    -----
    - Sloped width computed as: building_width / cos(theta).
    - Packs full panels only (no cutting), tries both orientations.
    """
    if building_length_m <= 0 or building_width_m <= 0:
        return 0.0, 0

    # convert inputs
    theta = math.radians(roof_angle_deg)
    cos_theta = math.cos(theta)
    if cos_theta <= 0:
        # roof angle >= 90° is non-physical here
        return 0.0, 0

    # Sloped width of the roof (meters)
    sloped_width_m = building_width_m / cos_theta

    # Panel dimensions in meters
    pw_m = panel_width_mm / 1000.0
    ph_m = panel_height_mm / 1000.0

    # Portrait packing (width along length, height along slope)
    cols_portrait = int(building_length_m // pw_m)
    rows_portrait = int(sloped_width_m  // ph_m)
    n_portrait = max(0, cols_portrait) * max(0, rows_portrait)

    # Landscape packing (height along length, width along slope)
    cols_land = int(building_length_m // ph_m)
    rows_land = int(sloped_width_m  // pw_m)
    n_land = max(0, cols_land) * max(0, rows_land)

    n_panels = max(n_portrait, n_land)
    total_capacity_kW = (n_panels * panel_power_Wp) / 1000.0
    return total_capacity_kW, n_panels


# --- Call the function with example inputs ---
pv_capacity_kw, num_panels = calculate_pv_size(
    building_length_m=30,   # meters
    building_width_m=10,     # meters
    roof_angle_deg=22       # degrees
)

# --- Display the results ---
print(f"Number of PV panels: {num_panels}")
print(f"Total PV capacity: {pv_capacity_kw:.2f} kW")


    # =============================================================================
    # This section is a common way to incorporate code that you want to run if the 
    # script is executed directly, but will be ignored if the script is 
    # imported as a module into another. 
    # 
    # It separates the executable part of the script from the part that defines
    # reusable components e.g. functions.
    # 
    # This is useful way of testing the code or providing examples of how to 
    # use the code.
    # =============================================================================
    

