import random


class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0,
        }
        self.set_env()

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(
            random.uniform(18, 30), 2
        )

        self.env_values["mars_base_external_temperature"] = round(
            random.uniform(0, 21), 2
        )
        self.env_values["mars_base_internal_humidity"] = round(
            random.uniform(50, 60), 2
        )
        self.env_values["mars_base_external_illuminance"] = round(
            random.uniform(500, 715), 2
        )
        self.env_values["mars_base_internal_co2"] = round(
            random.uniform(0.02, 0.1), 3
        )  # CO2는 소수점 셋째 자리까지
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values


ds = DummySensor()
ds.set_env()
print("set_env() 호출 후 환경 값:")
print(ds.get_env())
print("\nget_env() 호출 결과:")
env_data = ds.get_env()
for key, value in env_data.items():
    print(f"- {key}: {value}")
# # get_env()를 호출하여 값을 확인합니다.
# print("\nget_env() 호출 결과:")
# env_data = ds.get_env()
# for key, value in env_data.items():
#     print(f"- {key}: {value}")
