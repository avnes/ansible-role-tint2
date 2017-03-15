import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_conky_file(File):
    f = File('/home/ansible-test-user/.config/tint2/tint2rc')

    assert f.exists
    assert f.user == 'ansible-test-user'
    assert f.group == 'ansible-test-user'
    assert f.mode == 0o700
