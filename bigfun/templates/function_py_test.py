CACHE = {}

class Cache:

    def get(self, key):
        pass

    def set(self, key, value):
        pass

cache = Cache()

{{ init_code }}

def run():
    {% for name, value, type in arguments %}
    {% if type == 'string' and value is not none %}
    {{ name }} = {{ value | tojson }}
    {% else %}
    {{ name }} = {{ value }}
    {% endif %}
    {% endfor %}

    {{ code | indent(4) }}

result = run()
print(result)
