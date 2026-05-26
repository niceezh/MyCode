class Badge {

    public String print(Integer id, String name, String department) {
        department = department == null ? "OWNER" : department.toUpperCase();
        String common = String.format("%s - %s", name, department);
        return id == null ? common : String.format("[%d] - %s", id, common);
    }

}
