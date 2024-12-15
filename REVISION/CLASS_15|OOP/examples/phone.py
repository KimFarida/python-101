class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False
        self.apps = []

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON")

    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"Installed {app_name}")

    def view_apps(self):
        return print('|'.join(self.apps))

    def uninstall_app(self, app_name):
        if app_name in self.apps:
            self.apps.remove(app_name)
            print(f"Uninstalled {app_name}")
        else:
            print('App Not Found')

    # Create a method that turns of the phone and if the phone is aLready off, say so and
    #do nothing




# Each phone is unique
iphone = Phone("Apple", "iPhone 13")
android = Phone("Samsung", "S21")

iphone.turn_on()
iphone.install_app('Whatsapp')
iphone.install_app('Instagram')
iphone.view_apps()
iphone.uninstall_app('Twitter')
iphone.uninstall_app('Instagram')
iphone.view_apps()