VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Global Configs
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision 'shell', path: 'bootstrap.sh'

  config.vm.synced_folder "", "/home/vagrant/trail_tracker"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--usb", "off"]
  end


  # https://www.vagrantup.com/docs/provisioning/salt.html
  # This is where Salt configuration would go

  # Configures the Trail Tracker box
  config.vm.define "tracker", primary: true do |dev|
    dev.vm.hostname = "tracker.dev"

    dev.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "3072"]
    end

    # Vagrant assigns static addresses to the interface by editing
    # /etc/network/interfaces and iterates up/down after the main debian
    # interface config phase. This means that routes added earlier in the
    # config phase may be lost. It is best to auto_config: false and explicitly
    # put the configuration into the VM.
    dev.vm.network :private_network, ip: "10.10.6.66", auto_config: false
  end

end # Vagrant.configure
