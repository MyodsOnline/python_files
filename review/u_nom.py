from dataclasses import dataclass


@dataclass
class VoltageLimit:
    u_nom: float
    u_min: float
    u_max: float

def get_voltage_limit():
    # Номинальные и наибольшие рабочие напряжения соотвественно:
    Unom_set = [35, 67, 110, 150, 220, 330, 400, 500, 750]
    Umax_set = [40.5, 77, 126, 172, 252, 363, 420, 525, 787]
    # Коэффициент минимально допустимого напряжения доаварийной схемы:
    k_Umin_set = 1.1 * 0.7
    Umin_set = [u * k_Umin_set for u in Unom_set]
    voltage_limit = [
        VoltageLimit(u_nom=u_nom, u_min=u_min, u_max=u_max)
        for (u_nom, u_min, u_max) in zip(Unom_set, Umin_set, Umax_set)
    ]
    # return voltage_limit
    print(voltage_limit)


if __name__ == '__main__':
    get_voltage_limit()
