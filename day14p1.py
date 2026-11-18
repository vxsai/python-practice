#quest on unit test lecture on a kinematics question


def calc_ke(mass, velocity):
	if mass <= 0:
		return 0.0
	return round(0.5*mass*(velocity**2), 2)
